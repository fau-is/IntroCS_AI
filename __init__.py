import check50

import check50


def parse_tasks_txt(path: str = "tasks.txt"):
    """
    Parse tasks.txt into a list of events.
    Each event: {"id": int, "status": int, "name": str, "line": int}
    Raises check50.Failure on format violations.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise check50.Failure("tasks.txt not found. Your program must generate tasks.txt.")
    except Exception as e:
        raise check50.Failure(f"Could not read tasks.txt: {e}")

    events = []
    seen_ids = set()

    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not line or line.startswith("#"):
            continue

        parts = line.split("\t")
        if len(parts) < 3:
            raise check50.Failure(
                f"Invalid format in tasks.txt at line {idx}: "
                f"expected 3 tab-separated fields (id, status, name), got {len(parts)}.\n"
                f"Line content: {repr(line)}"
            )

        task_id_str = parts[0].strip()
        status_str = parts[1].strip()
        name = "\t".join(parts[2:])  # allow tabs in the remainder if students ever choose to; spec can forbid it

        if not task_id_str.isdigit():
            raise check50.Failure(
                f"Invalid task_id at line {idx}: expected integer >= 1, got {repr(task_id_str)}."
            )
        task_id = int(task_id_str)
        if task_id < 1:
            raise check50.Failure(
                f"Invalid task_id at line {idx}: must be >= 1, got {task_id}."
            )
        if task_id in seen_ids:
            raise check50.Failure(
                f"Duplicate task_id in tasks.txt at line {idx}: id {task_id} appears more than once."
            )
        seen_ids.add(task_id)

        if status_str not in ("0", "1"):
            raise check50.Failure(
                f"Invalid status at line {idx}: expected 0 or 1, got {repr(status_str)}."
            )
        status = int(status_str)

        if name.strip() == "":
            raise check50.Failure(
                f"Invalid task_name at line {idx}: task_name must be non-empty."
            )

        events.append({"id": task_id, "status": status, "name": name, "line": idx})

    return events


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
    """Parse tasks.txt into a list of events"""
    try:
        check50.run("python3 tracker.py add Task_A").exit(0)
        check50.run("python3 tracker.py add Task_B").exit(0)
        check50.run("python3 tracker.py finish 2").exit(0)
        check50.run("python3 tracker.py add Task_C").exit(0)
        check50.run("python3 tracker.py add Task_D").exit(0)
        check50.run("python3 tracker.py delete 3").exit(0)
    except:
        raise check50.Failure("Cannot run finish operation sequence with command sequence")

    check50.exists("tasks.txt")

    events = parse_tasks_txt("tasks.txt")

    # Minimal sanity conditions (you can relax/tighten)
    if len(events) == 0:
        raise check50.Failure("tasks.txt contains no task entries (only comments/blank lines).")

    if len(events) != 3:
        raise check50.Failure("tasks.txt contains wrong number of task entries.")

    if events[1]["status"] != "1" :
        raise check50.Failure("tasks1 has wrong status")

    if  events[0]["id"] != "1":
        raise check50.Failure("tasks0 has wrong id")

    if events[1]["status"] != "1" or events[0]["id"] != "1" or events[2]["name"] != "Task_D":
        raise check50.Failure("tasks.txt has wrong entries")

