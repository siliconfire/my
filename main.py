# github.com/siliconfire

print("\n")

import sys
import time
import hmac
import hashlib
import struct

use_gui = True
try:
    import tkinter as tk
except ImportError:
    print("[!] | tkinter doesn't seem to be installed. \n    | The GUI will be disabled for this session.\n\n")
    use_gui = False
try:
    from tkinter import ttk, messagebox
except ImportError:
    if use_gui != False:
        print("[!] | tkinter seems to be installed, but its components aren't. \n    | Please let me know if you get this error. (#2)\n    | The GUI will be disabled for this session.\n\n")


CODE_INTERVAL_TIME = 1000 * 60


def main():

    if use_gui:
        root = tk.Tk()
        root.title("code-generator (PoC)")

        def submit_action():
            key_value = key_entry.get()
            if ' ' in key_value or '\n' in key_value:
                warning_message = "WARNING:\n\nThe key you entered contains whitespaces.\nPlease check and verify that there are no spaces/newlines in your key."
                response = messagebox.askquestion("Whitespace Warning", warning_message + "\n\nDo you want to continue anyway?")
                if response == 'yes':
                    access_code, expiration_time = calculate_code(key_value)
                    show_access_code(access_code, expiration_time)
            else:
                access_code, expiration_time = calculate_code(key_value)
                show_access_code(access_code, expiration_time)

        def switch_to_cli_action():
            root.destroy()
            run_cli()

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(mainframe, text="Enter secret here:").grid(column=1, row=1, sticky=tk.W)
        key_entry = ttk.Entry(mainframe, width=40)
        key_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

        submit_button = ttk.Button(mainframe, text="Submit", command=submit_action)
        submit_button.grid(column=2, row=2, sticky=tk.W)

        switch_button = ttk.Button(mainframe, text="Switch to CLI", command=switch_to_cli_action)
        switch_button.grid(column=2, row=3, sticky=tk.W)

        root.mainloop()

    else:
        run_cli()

def calculate_code(key_value):
    code_valid_time = 1000 * 3600  # 1000ms (a second) * 3600 = 60 minutes

    timestamp_ms = int(time.time() * 1000)

    interval = timestamp_ms // code_valid_time
    interval_beginning_timestamp_ms = interval * code_valid_time
    adjusted_timestamp = interval_beginning_timestamp_ms // CODE_INTERVAL_TIME

    big_endian_timestamp = struct.pack(">Q", adjusted_timestamp)

    mac = hmac.new(key_value.encode(), big_endian_timestamp, hashlib.sha1)
    digest = mac.digest()

    offset = digest[-1] & 0xf

    result = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7fffffff

    access_code = result % 1000000  # Dividing result to 1000000 to get the code

    valid_to_ms = interval_beginning_timestamp_ms + code_valid_time

    return access_code, valid_to_ms


def show_access_code(access_code, expiration_time):
    access_code_window = tk.Toplevel()
    access_code_window.title("Access Code")

    ttk.Label(access_code_window, text=f"Access Code: {access_code:06}", font=("Helvetica", 20)).pack(padx=20, pady=10)

    def update_time_label():
        remaining_seconds = max(0, (expiration_time - int(time.time() * 1000)) // 1000)
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        time_label.config(text=f"Expires in: {minutes:02}:{seconds:02}")
        if remaining_seconds > 0:
            access_code_window.after(1000, update_time_label)

    time_label = ttk.Label(access_code_window, text="", font=("Helvetica", 12))
    time_label.pack(pady=10)

    update_time_label()

    close_button = ttk.Button(access_code_window, text="Close", command=access_code_window.destroy)
    close_button.pack(pady=10)

    access_code_window.mainloop()


def run_cli():
    if len(sys.argv) < 2:
        print(f"TIP | You can also pass the secret by: {sys.argv[0]} <secret>\n\n", file=sys.stderr)
        key_value = input("Type secret here: ")
    else:
        key_value = sys.argv[1]

    if key_value == "":
        print("cmon, you have to type something\n\n")
        time.sleep(1.5)
    else:
        displayAccessCode(key_value)

def displayAccessCode(key_value):
    access_code, expiration_time = calculate_code(key_value)
    print(f"\n\n\n\n\n-------------------------\nSecret: {key_value}\n\n")
    print(f"Access Code: {access_code:06}")
    print(f"Expires in: {calculate_remaining_time(expiration_time)}")

def calculate_remaining_time(expiration_time):
    remaining_seconds = max(0, (expiration_time - int(time.time() * 1000)) // 1000)
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    main()
