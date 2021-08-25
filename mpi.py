import os
import webbrowser

#global variables and lists
#manjaro gaming setup command
mgsc = ('sudo pacman -Syyu --noconfirm', 'sudo pacman -S --noconfirm yay', 'yay -S --noconfirm nvidia lutris mesa optimus-manager optimus-manager-qt steam game-mode', 'pip3 install protonup')
#blackarch setup
bs = ('sudo pacman -Syyu --noconfirm', 'sudo curl -O https://blackarch.org/strap.sh > strap.sh', 'sudo chmod +x strap.sh', 'sudo ./strap.sh')
#blackarch packages
bp = ('webapp', 'fuzzer', 'scanner', 'proxy', 'windows', 'dos', 'disassembler', 'cracker', 'voip', 'exploitation', 'recon', 'spoof', 'forensics', 'crypto', 'backdoor', 'networking', 'misc', 'defensive', 'wireless', 'automation', 'sniffer', 'binary', 'packer', 'reversing', 'mobile', 'malware', 'code-audit', 'social', 'honeypot', 'hardware', 'fingerprint', 'decompiler', 'config', 'debugger', 'firmware', 'bluetooth', 'database', 'automobile', 'nfc', 'tunnel', 'drone', 'unpacker', 'radio', 'keylogger', 'stego', 'scanner', 'anti-forensics', 'ids', 'gpu')
#archstrike packages
ap = ('scanners', 'misc', 'crackers', 'voip', 'forensics', 'wireless', 'recon', 'webapps', 'hardware', 'networking', 'defense', 'exploit', 'spoof', 'fingerprinting', 'crypto', 'backdoors', 'fuzzers', 'malware', 'honeypots', 'analysis', 'proxy', 'sniffers', 'tunnel', 'bruteforce', 'social-engineering',  'reverse', 'dns', 'debugging', 'decompile', 'intel', 'dos', 'ddos', 'enumeration', 'mitm', 'wordlists', 'exploits')

class mpi:
    def mgsc(self):
        for command in mgsc:
            print('>>>command in progress: ' + command)
            os.system(command)
            print('>>>command complete')

    def bs(self):
        for command in bs:
            print('>>>command in progress: ' + command)
            os.system(command)
            print('>>>command complete')

    def bp(self):
        for package in bp:
            print('>>>package in progress: ' + package)
            os.system('yay -S --noconfirm blackarch-' + package)
            print('>>>package completed')

    def aps(self):
        fo = open('/etc/pacman.conf', 'a')
        fo.write('[archstrike]\nServer = https://mirror.archstrike.org/$arch/$repo')
        fo.close()
        os.system('yay -S archstrike')

    def ap(self):
        for package in ap:
            print('>>>package in progress: ' + package)
            os.system('yay -S --noconfirm archstrike-' + package)
            print('>>>package completed')

def main():
    webbrowser.open('https://www.youtube.com/watch?v=E50L-JYWm3w')
    mpio = mpi()
    mpio.mgsc()
    mpio.bs()
    mpio.bp()
    mpio.aps()
    mpio.ap()

if __name__ == '__main__':
    print('>>>Welcome to Manjaro Post Installation tool, this tool will setup your manjaro for gaming as well as install all blackarch and archstrike tools, REMEMBER to run as ROOT now hit enter to continue and enjoy... go watch youtube or something')
    enter = input()
    main()
