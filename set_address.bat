@echo off
setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do (
   set /A argCount+=1
)
if %argCount% LSS 1 (
    echo "use get_hwid.bat <address>
    goto :EOF
)

python ModbusMessage.py -a %1 -c rregs -s 0 -P %RS485_COMPORT%

:EOF