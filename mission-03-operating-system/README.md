# Mission 3 — Operating Systems

## Mission objective

Understand how an operating system (OS) manages computer hardware and software, runs processes, uses memory and storage, organises files, and protects files with permissions.

> This guide uses macOS examples because the project is being worked on from a Mac. Commands and screens may differ on Windows or Linux. The observation tables are intentionally left for you to complete from your own computer.

## 1. What is an operating system?

An operating system is system software that manages the computer's hardware and provides services that applications use. It acts as an intermediary between applications/users and hardware.

Examples include macOS, Windows, Linux, Android and iOS.

### Main responsibilities

| Responsibility | What it means | Example |
|---|---|---|
| Process management | Starts, schedules and stops running programs | Running a browser |
| Memory management | Allocates and tracks RAM used by programs | Keeping a document editor open |
| File management | Organises files and directories | Saving a document in Documents |
| Device management | Coordinates hardware through drivers and system services | Using a keyboard or printer |
| User interface | Provides ways for people to interact with the computer | Desktop, windows and menus |
| Security and permissions | Controls who can access resources | Restricting access to a private file |
| Networking | Provides services for network communication | Connecting to Wi-Fi |

## 2. Programs, processes and process states

A **program** is a set of instructions stored as a file. A **process** is an instance of a program that is currently executing. A process has a process identifier called a **PID**.

Common simplified process states:

- **New:** the process is being created.
- **Ready:** it can run and is waiting for CPU time.
- **Running:** its instructions are currently being executed.
- **Waiting / blocked:** it is waiting for an event, such as input or a file operation.
- **Terminated:** it has finished or has been stopped.

A process can move between these states. Operating systems schedule processes so that many applications can appear to run at the same time.

### Observe processes on macOS

Run:

```bash
ps
ps -A | head -n 10
```

The `ps` command reports process information. `ps -A` requests processes across the system; `head -n 10` limits the displayed output to the first ten lines. The exact columns can vary.

To find a process by name, for example Terminal:

```bash
pgrep -fl Terminal
```

You can also open **Activity Monitor** using Spotlight (press Command-Space and type “Activity Monitor”). Select the **CPU** tab to inspect process names, CPU use and PIDs. Select **Memory** to inspect memory use. Apple explains that Activity Monitor can show process information and memory/CPU usage. See [Apple's Activity Monitor User Guide](https://support.apple.com/guide/activity-monitor/welcome/mac).

**Safety:** Do not terminate unfamiliar system processes. For this assignment, observe only. If an app is unresponsive, use normal app quit options or consult a trusted guide before force-quitting a process.

## 3. Memory and storage

**RAM (Random Access Memory)** is fast, temporary working memory used by active programs and the operating system. Its contents are generally lost when the computer is powered off.

**Storage** (such as an SSD) keeps files and applications even when the computer is turned off. Storage is usually much larger than RAM but works differently.

| RAM | Storage (SSD / hard drive) |
|---|---|
| Temporary working area | Long-term file storage |
| Used by running programs | Stores documents, applications and the OS |
| Usually cleared when power is off | Keeps data when power is off |
| Measured in GB | Measured in GB or TB |

### Inspect storage from Terminal

```bash
df -h
```

This displays mounted file systems and their used/available space in human-readable units. It may show several system, virtual or external volumes; do not assume every row is a separate physical disk.

To inspect a folder's size:

```bash
du -sh ~/Desktop
```

This reports the total size of the Desktop directory. Your result will depend on the files stored there.

You can also use **Activity Monitor → Memory** to observe memory pressure and per-process memory use. The numbers change while applications run.

## 4. Files, directories and paths

A **file** stores information, such as text, an image or a program. A **directory** (folder) groups files and other directories.

- An **absolute path** describes a location from the filesystem root. Example: `/Users/your-account/Documents/notes.txt`.
- A **relative path** describes a location starting from the current working directory. Example: `Documents/notes.txt`.
- `.` means the current directory.
- `..` means the parent directory.
- `~` is shorthand for the current user's home directory in the shell.

Try these safe commands:

```bash
pwd
ls
cd ~
pwd
ls
cd ~/Desktop
pwd
```

Do not copy a real personal path into a public repository if it reveals your account name. Use placeholders such as `/Users/your-account/` in written examples.

## 5. Users and file permissions

Permissions determine which users may read, change or execute a file, or access a directory.

The three basic permission symbols are:

- **r — read:** view file contents; for a directory, list its entries (subject to other permissions).
- **w — write:** change a file; for a directory, create, remove or rename entries (subject to other permissions).
- **x — execute:** run an executable file; for a directory, traverse/access entries when the other permissions allow it.

Permissions are commonly displayed for three classes:

- **Owner:** the file's owning user.
- **Group:** users in the file's group.
- **Others:** everyone else.

Example permission string:

```text
-rwxr-xr--
```

Interpretation:
- The first character `-` indicates a regular file.
- Owner: `rwx` (read, write, execute).
- Group: `r-x` (read and execute).
- Others: `r--` (read only).

A directory may begin with `d` instead of `-`.

### Inspect permissions

```bash
ls -l
ls -ld ~/Desktop
```

The first column shows permission bits. The owner and group are shown in later columns. The exact output depends on your computer and account.

### Practise changing permissions safely

Use a new practice directory and file, not system files:

```bash
mkdir -p ~/Desktop/os-permission-practice
cd ~/Desktop/os-permission-practice
printf "Permission practice only.\n" > sample.txt
ls -l sample.txt
chmod 600 sample.txt
ls -l sample.txt
chmod 644 sample.txt
ls -l sample.txt
```

On macOS and other Unix-like systems:
- `chmod 600` gives the owner read/write permission and removes group/other permissions.
- `chmod 644` gives the owner read/write permission and group/others read permission.

The commands above affect only the practice file. Do not use `sudo` or change permissions on system directories for this assignment.

## 6. Command reference

| Command | Purpose |
|---|---|
| `ps` | Show process information |
| `ps -A` | Request a listing of all processes |
| `pgrep -fl name` | Find processes matching a name |
| `df -h` | Show filesystem space in readable units |
| `du -sh path` | Show a directory's total size |
| `pwd` | Print the current working directory |
| `ls -l` | List files with permissions and details |
| `ls -ld path` | Show details for the directory itself |
| `chmod 600 file` | Set owner read/write permissions |
| `chmod 644 file` | Set owner read/write and group/others read permissions |

## 7. My observations — complete on your computer

Do not invent these values. Run the commands or open Activity Monitor and write down a short, privacy-safe summary.

| Activity | My observation |
|---|---|
| One process name and its PID from Activity Monitor or `ps` | _Fill in after observing_ |
| What the CPU tab shows | _Fill in after observing_ |
| What the Memory tab shows (no personal details) | _Fill in after observing_ |
| One general storage observation from `df -h` | _Fill in after observing; avoid publishing personal volume names_ |
| Permission string before and after `chmod` | _Fill in after running the practice_ |
| Difference between an absolute and relative path | _Explain in your own words_ |

## 8. Questions and answers

**1. What is the purpose of an operating system?**

It manages hardware and software resources and provides common services so applications can run. It also provides a user interface and security controls.

**2. What is the difference between a program and a process?**

A program is stored instructions. A process is a running instance of a program, with its own execution state and resources.

**3. What is a PID?**

A PID is a process identifier used by the operating system to identify a process.

**4. What is the difference between RAM and storage?**

RAM is temporary working memory for active tasks. Storage keeps files and applications for long-term use.

**5. What is the difference between an absolute and a relative path?**

An absolute path starts from the filesystem root. A relative path is interpreted from the current working directory.

**6. What do r, w and x mean?**

Read, write and execute. Their exact effect differs slightly for files and directories.

**7. Why are permissions important?**

They help prevent unauthorised users from reading, changing or running files and help protect the system and user data.

## 9. Reflection — answer in your own words

1. How does an operating system help applications use computer hardware?
2. Why can several processes appear to run at the same time?
3. Why does a computer need both RAM and long-term storage?
4. Why should you avoid changing permissions on system files?
5. Which command or Activity Monitor view helped you understand your computer best?

## 10. Completion checklist

- [ ] I can explain at least four responsibilities of an operating system.
- [ ] I can explain the difference between a program and a process.
- [ ] I observed a process and its PID.
- [ ] I can explain RAM versus storage.
- [ ] I ran `df -h` and understand what it reports.
- [ ] I can explain absolute and relative paths.
- [ ] I can explain owner, group and others, and r/w/x.
- [ ] I ran the permission exercise only inside the practice directory.
- [ ] I completed the observation table and reflection in my own words.
- [ ] I added evidence only if required, with private information hidden.

## Evidence and references

- [Apple — Activity Monitor User Guide](https://support.apple.com/guide/activity-monitor/welcome/mac)
- [Apple — View information about Mac processes](https://support.apple.com/en-au/guide/activity-monitor/actmntr1001/mac)

If your assignment requires screenshots, capture your own Activity Monitor and Terminal observations. Hide usernames, personal paths, serial numbers and other identifying information before uploading them.
