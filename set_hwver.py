#!/usr/bin/python3
import ModbusMessage
import click

@click.command()
@click.option('--hwver','-d', type=int, required=True, help='VMA modbus address')
@click.option('--ComPort', '-P', type=str, default = '/dev/ttyS0', help='Comm port name')
@click.option('--Baudrate', '-r', type=int, default = 38400, help='Communication baud rate')
@click.option('--Verbose', '-V', is_flag=True, help='Show aditional modbus details')   
def main(hwver:int, comport:int, baudrate:int, verbose:bool):
    params = ['-a', 0, '-c', 'wreg', '-s', '34', '-d', hwver,'-P', comport, '-r', baudrate]
    if verbose:
        params.append('-V')
    ModbusMessage.main(params)

if __name__ == '__main__':
    main()
