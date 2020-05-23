@Echo off
set CURRPATH=%CD%
if %1 == -l goto learning
if %1 == -p goto project
Echo Argument action not found
pause
goto end
:learning
cd D:/Academics/Learning/test_runs/
goto continue
:project
cd D:/Academics/Projects/
:continue
mkdir %2
cd %2
type nul > README.txt  
set NEWPATH=%CD%
git init
git add .
git commit -m "Initial Commit"
python D:\Academics\Learning\test_runs\Automation\github.py %2 %CURRPATH%
git push origin master
cd %CURRPATH%
code %NEWPATH%
:end
pause
