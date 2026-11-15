# Mission 2 — Terminal

## Goal

Learn how to navigate folders, inspect files, create and edit files, copy and rename them, and use command options and pipes safely from the macOS Terminal.

> **Important:** This README is a guided practical. The commands below are ready to run, but the personal command log and reflection should be filled in after running them on your own Mac. Do not claim a command was tested unless you ran it.

## 1. Open Terminal and identify your location

Open **Terminal** on macOS (Applications → Utilities → Terminal), then run:

```bash
pwd
```

- `pwd` means *print working directory*.
- It prints the full path of the directory Terminal is currently using.

List the visible files and folders:

```bash
ls
```

Show a detailed listing, including hidden entries:

```bash
ls -la
```

Useful points:
- `-l` requests a long, detailed listing.
- `-a` includes hidden entries whose names begin with a dot.
- Options (also called flags) change how a command behaves.

## 2. Navigate between directories

```bash
cd ~/Desktop
pwd
cd ..
pwd
cd ~
pwd
```

- `cd` changes the current directory.
- `~` represents your home directory.
- `..` means the parent directory.
- An absolute path starts from the filesystem root; a relative path is interpreted from the current directory.

## 3. Create a safe practice area

The following exercise creates and changes files only inside a dedicated folder on your Desktop. If the folder already exists, the commands reuse it; the file contents below are deliberately set to the stated practice text.

```bash
mkdir -p ~/Desktop/terminal-practice
cd ~/Desktop/terminal-practice
pwd
```

Create a text file and write its first line:

```bash
printf "First line: learning Terminal.\n" > notes.txt
```

Append a second line without replacing the first:

```bash
printf "Second line: practising file commands.\n" >> notes.txt
```

Read the file:

```bash
cat notes.txt
```

Expected contents:

```text
First line: learning Terminal.
Second line: practising file commands.
```

**Difference between `>` and `>>`:**
- `>` creates a file or replaces its existing contents.
- `>>` appends text to the end of a file.

## 4. Copy, rename, and inspect files

```bash
cp notes.txt notes-backup.txt
ls -l
mv notes-backup.txt notes-copy-renamed.txt
ls -l
cat notes-copy-renamed.txt
```

- `cp` creates a copy and keeps the original.
- `mv` moves a file or renames it.
- `cat` prints file contents.

Compare the original and copy:

```bash
diff notes.txt notes-copy-renamed.txt
```

No output from `diff` means the two files have matching contents.

## 5. Use command options and pipes

Show only the first five lines of a listing:

```bash
ls -la | head -n 5
```

Count the lines in the practice file:

```bash
wc -l notes.txt
```

Search for the word `Terminal`:

```bash
grep "Terminal" notes.txt
```

A **pipe** (`|`) sends the output of the command on its left to the command on its right. In the example, the listing from `ls -la` becomes the input to `head`.

## 6. Get help

```bash
man ls
```

This opens the manual page for `ls`. Press `q` to quit the manual viewer.

Many commands also support a help option, but the exact option varies by command. On macOS, `man command-name` is a dependable place to start.

## 7. Remove practice files safely

First check that you are in the practice directory:

```bash
pwd
ls -la
```

Remove only the two files created in this exercise:

```bash
rm notes.txt notes-copy-renamed.txt
```

Then verify:

```bash
ls -la
```

**Safety:** `rm` normally does not move files to the Trash. Never run broad deletion commands such as `rm -rf` unless you fully understand the path and consequences.

## 8. Command reference

| Command | Purpose |
|---|---|
| `pwd` | Print the current working directory |
| `ls` | List directory contents |
| `ls -la` | Include hidden entries and detailed information |
| `cd path` | Change directory |
| `mkdir -p path` | Create a directory, including missing parent directories |
| `printf` | Print formatted text; useful for writing predictable file contents |
| `cat file` | Display file contents |
| `cp source destination` | Copy a file |
| `mv source destination` | Move or rename a file |
| `diff file1 file2` | Compare two files |
| `head -n 5 file` | Display the first five lines |
| `wc -l file` | Count lines |
| `grep pattern file` | Find matching lines |
| `man command` | Open a command's manual |
| `rm file` | Delete a file |

## 9. My practical command log

Complete this table after running the commands on your own Mac. Record a short, non-sensitive observation; do not paste private paths or account information.

| Command | What I observed on my Mac |
|---|---|
| `pwd` | _Fill in after running_ |
| `ls` | _Fill in after running_ |
| `ls -la` | _Fill in after running_ |
| `mkdir -p` | _Fill in after running_ |
| `cat` | _Fill in after running_ |
| `cp` | _Fill in after running_ |
| `mv` | _Fill in after running_ |
| `ls -la | head -n 5` | _Fill in after running_ |
| `grep` | _Fill in after running_ |
| `diff` | _Fill in after running_ |

## 10. Reflection

Answer in your own words after completing the exercise:

1. Which command was most useful to you, and why?
2. What is the difference between an absolute path and a relative path?
3. What is the difference between `>` and `>>`?
4. How are `cp` and `mv` different?
5. What does a pipe (`|`) do?
6. Why should you check the current directory before deleting files?

## Completion checklist

- [ ] I ran `pwd`, `ls`, and `ls -la`.
- [ ] I navigated using `cd`.
- [ ] I created the practice directory.
- [ ] I created a file and appended a second line.
- [ ] I read the file using `cat`.
- [ ] I copied and renamed the file.
- [ ] I tried a pipe and a search command.
- [ ] I checked the directory before removing only the practice files.
- [ ] I completed the command log and reflection in my own words.

## Evidence

Add a screenshot of the Terminal exercise here only if your assignment asks for one. Before sharing, make sure it does not reveal private paths, usernames, tokens, or other personal information.
