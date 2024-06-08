class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def info(msg: str):
    print(f"{BColors.WARNING}{msg}{BColors.ENDC}")

def success(msg: str):
    print(f"{BColors.OKGREEN}{msg}{BColors.ENDC}")

def fail(msg: str):
    print(f"{BColors.FAIL}{msg}{BColors.ENDC}")

def comment(msg: str):
    print(f"{BColors.OKBLUE}{msg}{BColors.ENDC}")