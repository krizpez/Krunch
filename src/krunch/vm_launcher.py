# Virtual Machine Launcher Module

class VMLauncher:
    def __init__(self, vm_name):
        self.vm_name = vm_name
        self.process = None

    def start_vm(self):
        import subprocess
        command = ['qemu-system-x86_64', '-name', self.vm_name]
        self.process = subprocess.Popen(command)
        return self.process.pid

    def stop_vm(self):
        if self.process:
            self.process.terminate()
            self.process = None
        else:
            raise Exception('VM is not running.') 

    def is_running(self):
        return self.process is not None and self.process.poll() is None

