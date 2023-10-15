import sys
print(sys.version)
print(sys.version_info)

print(sys.argv)
#print(sys.orig_argv)

if len(sys.argv)<3:
    print("Не указаны папка-источник и папка-назначение")
    exit(1)

source_dir = sys.argv[1]
dest_dir = sys.argv[2]
print('source dir:', source_dir)
print('dest dir:', dest_dir)