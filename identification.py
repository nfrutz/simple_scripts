printers_id = 0
heads_id = 0
platforms_id = 0


def pick_an_id(module_name=""):
    """
    Generate a new ID for a new module printer, head or platform
    :param module_name: String {printer, head, platform}
    :return:
    """
    if module_name == "printer":
        global printers_id
        printers_id += 1
        return printers_id
		
    elif module_name == "head":
        global heads_id
        heads_id += 1
        return heads_id
		
    elif module_name == "platform":
        global platforms_id
        platforms_id += 1
        return platforms_id
		
    else:
        print("Name Unknown")
        return -1


if __name__ == "__main__":
    for name in 2*["printer", "head", "platform"]:
        print("Module %s has ID: %d" % (name, pick_an_id(name)))
