import streamlit as st
import subprocess
import platform
import time

st.set_page_config(page_title="Study Ninja - Lets You Focus 🥷", page_icon="🥷", layout="wide")
st.header("Study Ninja - Lets You Focus 🥷")

def set_dnd_mode(enable=True):
    system = platform.system()

    if system == "Windows":
        # Windows PowerShell command for Focus Assist
        subprocess.run('powershell -Command "New-Item -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion -Name QuietHours -Force"', shell=True)
        level = 2 if enable else 0
        command = f'powershell -Command "Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\QuietHours -Name QuietHoursEnabled -Value {level} -Type DWord"'
        subprocess.run(command, shell=True)

    elif system == "Darwin":
        # macOS - Requires permissions to control DND mode
        dnd_status = "true" if enable else "false"
        subprocess.run(f'defaults -currentHost write com.apple.notificationcenterui doNotDisturb -bool {dnd_status}', shell=True)
        subprocess.run("killall NotificationCenter", shell=True)  # Restart Notification Center to apply changes

    elif system == "Linux":
        # GNOME desktops only (e.g., Ubuntu)
        status = "true" if enable else "false"
        subprocess.run(f"gsettings set org.gnome.desktop.notifications show-banners {status}", shell=True)

    else:
        st.warning("DND mode control is not available for this platform.")

def dnd_mode_for_duration(duration_hours):
    st.write("Turning on DND mode...")
    set_dnd_mode(enable=True)
    time.sleep(duration_hours * 3600)  # Convert hours to seconds
    st.write("Turning off DND mode...")
    set_dnd_mode(enable=False)

# Streamlit interface for selecting duration in hours
duration_hours = st.number_input("Enter DND duration (hours)", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Turn on DND mode"):
    dnd_mode_for_duration(duration_hours)

def upload_notes():
    notes = st.file_uploader("Choose a PDF", type="pdf")
    return notes

upload_notes()

