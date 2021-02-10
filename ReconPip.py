#!/usr/bin/env python3
"""Multi-Tool Recon Python Wrapper."""
import os
from typing import List

print("""
01010010 01100101 01100011 01101111 01101110 01010000 01101001 01110000 
0                                                                     0
1    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██████╗ ██╗██████╗    1
1    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔══██╗██║██╔══██╗   1
0    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║██████╔╝██║██████╔╝   1
0    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔═══╝ ██║██╔═══╝    0
1    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║     ██║██║        0
1    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝        1
0                                                                     0
01010010 01100101 01100011 01101111 01101110 01010000 01101001 01110000 


                            RECONPIP : v1.0.0
                        MULTI-TOOL RECON WRAPPER

""")

def _get_url(tool_name: str) -> str:
    url: str
    if tool_name == 'wafd':
        url = input('Type the base URL you wish to run through detector (do not include "www."):\n\t')
    elif tool_name == 'scn':
        url = input('Type the base URL you wish to scan (do not include "www."):\n\t')
    elif tool_name == 'gth':
        url = input('Type the base URL from which you wish to gather data (do not include "www."):\n\t')
    return url


def _get_log_name() -> str:
    log_name: str = input(
        'Type the log name to be created/appended (include file extension):\n\t'
    )
    return log_name


def _get_command(tool_name: str) -> str:
    #
    # Get the url and log name
    #
    print(f'{tool_name.upper()} starting...')
    url: str = _get_url(tool_name)
    log_name: str = _get_log_name()
    #
    # Construct the command
    #
    command: str
    if tool_name == 'wafd':
        command = f'wafw00f -a {url} | tee -a {log_name}'
    #elif tool_name == 'exit':
    #    keyboard.send(ctrl+c)
    elif tool_name == 'scn':
        command = f'sslyze {url}:443 | tee -a {log_name}'
    elif tool_name == 'gth':
        command = f'theharvester -d {url} -b bing | tee -a {log_name}'
    else:
        print('Invalid source entry.  Try again...')
    #
    # Return the command
    #
    return command


def main():
    """Recon does something...."""
    done_logging: bool = False
    valid_tools: List[str] = ['wafd', 'scn', 'gth']
    while not done_logging:
        tool_name = input(
            '\nWhich tool would you like to use?\n'
            '\tType WAFD for WAF Detector\n'
            '\tType SCN for SSL/TLS Scanning Library\n'
            '\tType GTH for general information gathering\n'
            '\tType EXIT to exit\n'
        )
        tool_name: str = tool_name.lower()
        if tool_name.lower() in valid_tools:
            command: str = _get_command(tool_name)
            os.system(command)
        elif tool_name.lower() == 'exit':
            done_logging: bool = True
        else:
            print('\tInvalid input. Try again...\n')
    print('\nExiting program.  Have a good day!\n')



if __name__ == '__main__':
    main()
