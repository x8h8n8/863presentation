/*************************************************************************
	> File Name: hmfs_show.c
	> Author: Weiyu Cheng
	> Mail:
	> Created Time: 2017年09月22日 星期五 15时34分14秒
 ************************************************************************/

#include<stdio.h>
#include<sys/vfs.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>

// 使用说明：
// gcc -o hmfs_show hmfs_show.c
// ./hmfs_show dir （dir为hmfs挂载的目录，测试时也可使用其他文件系统目录）
// 程序会返回进程pid，之后保持在后台运行，可通过kill -9 pid终止；
// 运行结果保存在 hmfs_status.txt 中
// 程序每秒更新一次文件，频率可通过sleep(t)函数参数调整，t即为休眠的秒数；
// 格式为：NVM 已使用内存 总占用内存 （单位为MB）

int main(int argc, char** argv)
{
        char doc[]="hmfs_status.txt";

    if(argc!=2){
        printf("usage: ./hmfs_show absolute_path_of_hmfs_dir\n");
        return -1;
    }

    if(daemon(1,1)<0){
        perror("daemon");
        return 1;
    }

    pid_t pid = getpid();
    printf("Running in background, the pid is %d\n", pid);

    while(1)
    {
        struct statfs diskInfo;
        statfs(argv[1],&diskInfo);
        unsigned long long blocksize = diskInfo.f_bsize;// 每个block里面包含的字节数
        unsigned long long totalsize = blocksize * diskInfo.f_blocks;//总的字节数
        unsigned long long freeDisk = diskInfo.f_bfree*blocksize; //再计算下剩余的空间大小

        //int fd = open(doc, O_CREAT|O_WRONLY|O_TRUNC);
        int fd = creat(doc, S_IRWXU|S_IROTH);
        char content[128];
        int len = sprintf(content, "NVM %lld %lld\n", (totalsize-freeDisk)>>20, totalsize>>20);
        write(fd, content, len);
        close(fd);
        sleep(1);
    }

     return 0;

}
