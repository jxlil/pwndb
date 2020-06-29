#!/usr/bin/env python3

from pwndb import __version__


def print_banner():
    print(
        f"""    
                                 _ _     
                                | | |    
         _ ____      ___ __   __| | |__  
        | '_ \ \ /\ / / '_ \ / _` | '_ \ 
        | |_) \ V  V /| | | | (_| | |_) |
        | .__/ \_/\_/ |_| |_|\__,_|_.__/ 
        | |        Version: {__version__}
        |_|                              
        """
    )

