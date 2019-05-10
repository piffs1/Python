import os, pyperclip

print(os.name) #  'posix', 'nt', 'mac', 'os2', 'ce', 'java'.
for lst in os.environ.items(): # словарь переменных окружения, изменяемый
	print(lst)

print(os.getlogin()) # Имя пользователя

print(os.getpid()) # Текущий ID процесса

#os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True) - проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.
#os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True) - смена прав доступа к объекту (mode - восьмеричное число).
#os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True) - меняет id владельца и группы (Unix).
#os.makedirs ->Созданиме промежуточных директорий
#os.remove Удаление пути к файлу
#os.rename(src,dst) -> переименование из src в dst
#os.renames(old,new) -> переименовывание из old в new
#os.replace -> переименование с принудительнеой заменой
#os.rmdir удаляет пустую директорию
#os.removedirs(path) удаляет директорию, затем пытается удалить родительские рекурсивно, пока они пусты.
