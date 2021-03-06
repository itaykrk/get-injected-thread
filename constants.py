import os
import psutil
from winapi.kernel32 import MEM_IMAGE, MEM_COMMIT, MEM_FREE, MEM_RESERVE, MEM_MAPPED, MEM_PRIVATE, PAGE_NOACCESS, \
    PAGE_EXECUTE, PAGE_EXECUTE_READ, PAGE_EXECUTE_READWRITE, PAGE_EXECUTE_WRITECOPY, PAGE_READONLY, PAGE_READWRITE, \
    PAGE_WRITECOPY, PAGE_GUARD, PAGE_NOCACHE, PAGE_WRITECOMBINE, MEM_DECOMMIT, MEM_RELEASE, MEM_RESET, MEM_TOP_DOWN, \
    MEM_WRITE_WATCH, MEM_PHYSICAL

MEMORY_STATES_CONSTANTS = {
    MEM_COMMIT : "MEM_COMMIT",
    MEM_FREE : "MEM_FREE",
    MEM_RESERVE : "MEM_RESERVE"
}

MEMORY_TYPE_CONSTANTS = {
    MEM_IMAGE: "MEM_IMAGE",
    MEM_MAPPED: "MEM_MAPPED",
    MEM_PRIVATE: "MEM_PRIVATE"
}

MEMORY_PROTECTION_CONSTANTS = {
    PAGE_NOACCESS: "PAGE_NOACCESS",
    PAGE_EXECUTE: "PAGE_EXECUTE",
    PAGE_EXECUTE_READ: "PAGE_EXECUTE_READ",
    PAGE_EXECUTE_READWRITE: "PAGE_EXECUTE_READWRITE",
    PAGE_EXECUTE_WRITECOPY: "PAGE_EXECUTE_WRITECOPY",
    PAGE_READONLY: "PAGE_READONLY",
    PAGE_READWRITE: "PAGE_READWRITE",
    PAGE_WRITECOPY: "PAGE_WRITECOPY",
    PAGE_GUARD: "PAGE_GUARD",
    PAGE_NOCACHE: "PAGE_NOCACHE",
    PAGE_WRITECOMBINE: "PAGE_WRITECOMBINE",
    MEM_DECOMMIT: "MEM_DECOMMIT",
    MEM_RELEASE: "MEM_RELEASE",
    MEM_RESET: "MEM_RESET",
    MEM_TOP_DOWN: "MEM_TOP_DOWN",
    MEM_WRITE_WATCH: "MEM_WRITE_WATCH",
    MEM_PHYSICAL: "MEM_PHYSICAL"
}

MEMORY_PROTECTION_MODIFIERS_CONSTANTS = {
    PAGE_GUARD: "PAGE_GUARD",
    PAGE_NOCACHE: "PAGE_NOCACHE",
    PAGE_WRITECOMBINE: "PAGE_WRITECOMBINE"
}

BUFFER_SIZE = 1024  # bytes to dump from suspicious thread.
LESS_SUSPICIOUS_PROCESSES = ["vmware-vmx.exe", "SmartAudio3.exe"]

BLACKLIST_PROCESSES = [os.getpid(), 0, 4]  # Blacklist system process 4 and system idle process 0
secure_system_process = [p.pid for p in psutil.process_iter() if p.name() == ("Secure System")]
if secure_system_process:
    BLACKLIST_PROCESSES.append(secure_system_process.pop())