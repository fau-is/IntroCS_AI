import check50


@check50.check()
def check_file():
    '''tracker.py exists'''
    check50.exists("tracker.py")


@check50.check()
def run_tracker():
    '''run tracker.py'''
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
    except:
         raise check50.Failure("Cannot run tracker.py")

    check50.exists("tasks.txt")
    check50.exists("audit.txt")


@check50.check()
def functionality_check_add():
    """combined functionality"""
    #check50.run("rm -f tasks.txt audit.txt").exit(0)
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
    except:
        raise check50.Failure("Cannot run finish operation sequence with command add")


@check50.check()
def functionality_check_finish():
    """combined functionality"""
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
        check50.run("python3 tracker.py finish 2").exit(0)
    except:
        raise check50.Failure("Cannot run finish operation sequence with command finish")


@check50.check()
def functionality_check_delete():
    """combined functionality"""
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
        check50.run("python3 tracker.py finish 2").exit(0)
        check50.run("python3 tracker.py add Task_C").exit(0)
        check50.run("python3 tracker.py add Task_D").exit(0)
        check50.run("python3 tracker.py delete 3").exit(0)
    except Exception as e:
        raise check50.Failure("Cannot run finish operation sequence with command delete")

    try:
        check50.run("python3 tracker.py list").exit(0)
    except:
        raise check50.Failure("Cannot run finish operation sequence with command list")


@check50.check()
def functionality_check_file():
    """combined functionality"""
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
        check50.run("python3 tracker.py finish 2").exit(0)
        '''
        check50.run("python3 tracker.py add Task_C").exit(0)
        check50.run("python3 tracker.py add Task_D").exit(0)
        
        check50.run("python3 tracker.py delete 3").exit(0)
        '''
    except:
        raise check50.Failure("Cannot run finish operation sequence")

    check50.run(r"""bash -lc "cat > expected.txt << 'EOF'
    1	0	Task_A
    2	1	Task_B
    EOF
    " """).exit(0)

    check50.run(r"""bash -lc "cat > expected1.txt << 'EOF'
    1	0	Task_A
    2	1	Task_B
    EOF
    " """).exit(0)
    check50.exists("expected.txt")
    check50.exists("expected1.txt")
    check50.run("diff -u expected.txt expected1.txt").exit(0)


