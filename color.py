import os

green='color a' if os.name=='nt' else 'printf "\033[32m"'
red='color c' if os.name=='nt' else 'printf "\033[31m"'
reset='color' if os.name=='nt' else 'printf "\033[39m"'
