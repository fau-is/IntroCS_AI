import check50


@check50.check()
def check_file():
    '''tracker.py exists'''
    check50.exists("tracker.py")


@check50.check()
def run_file():
    '''run tracker.py'''
    try:
        check50.run("python3 tracker.py list").exit(0)
    except:
         raise check50.Failure("Cannot run tracker.py")


@check50.check()
def generates_tasks_file():
    """tasks.txt is generated"""
    check50.run("python3 tracker.py list").exit(0)
    check50.exists("tasks.txt")


@check50.check()
def generates_audit_file():
    """audit.txt is generated"""
    check50.run("python3 tracker.py list").exit(0)
    check50.exists("audit.txt")


@check50.check()
def add_task_runs():
    """add command runs"""
    check50.run("python3 tracker.py add Buy_milk").exit(0)



@check50.check()
def functionality():
    """combined functionality"""
    check50.run("rm -f tasks.txt audit.txt").exit(0)
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
    except:
        raise check50.Failure("Cannot run finish operation sequence with command add.py")



@check50.check()
def check():
    """combined functionality"""
    check50.run("rm -f tasks.txt audit.txt").exit(0)
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
    except:
        raise check50.Failure("Cannot run finish operation sequence with command add.py")



