import tkinter as tk
import requests
from bs4 import BeautifulSoup
import os
import re
import threading


# User agent to prevent Google from blocking the request
Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"# User agent to prevent Google from blocking the request


# Ensure that the directory exists, otherwise create it
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Clean the filename by removing the path and query parameters
def clean_filename_from_url(url):
    filename = re.search(r'[^/]+\.pdf', url)
    if filename:
        return filename.group(0)
    else:
        return "untitled.pdf"

# Search for PDFs on Google
def search_for_pdfs(query, num_results=10):
    search_url = f"https://www.google.com/search?q={query}&num={num_results}&as_filetype=pdf"
    headers = {"User-Agent": Agent} 
    pdfs_root_directory = "pdfs"  # Root directory to save PDFs

    topic = query.replace(" ", "_")
    ensure_directory_exists(pdfs_root_directory)

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            url = link.get('href')
            if url and url.endswith(".pdf"):
                pdf_response = requests.get(url)
                pdf_filename = os.path.join(pdfs_root_directory, topic, clean_filename_from_url(url))
                ensure_directory_exists(os.path.dirname(pdf_filename))
                with open(pdf_filename, 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                update_display(f"Downloaded: {pdf_filename}")

    except requests.exceptions.RequestException as e:
        update_display(f"An error occurred: {e}")

    # Enable the search button after the search is complete
    search_button.config(text="Search", state=tk.NORMAL)


# Update the display with a message
def update_display(message):
    display_text.config(state=tk.NORMAL)  # Allow editing
    display_text.insert(tk.END, message + "\n")# Add the message to the end of the widget
    display_text.config(state=tk.DISABLED)  # Disable editing


# Clear the display
def clear_display():
    display_text.config(state=tk.NORMAL)# Allow editing
    display_text.delete(1.0, tk.END)  # Clear all text in the widget
    display_text.config(state=tk.DISABLED)# Disable editing


# Send the input to the search function
def send_input():
    query = entry.get()# Get the query from the entry widget
    num_results = entry_2.get()# Get the number of results from the entry widget
    clear_display()  # Clear the update display
    update_display(f"Searching for '{query}'...")# Update the display with the query
    
    # Disable the search button while searching
    search_button.config(text="Searching...", state=tk.DISABLED, bg="orange")# Disable the search button while searching

    # Start the search in a separate thread to prevent blocking the UI
    search_thread = threading.Thread(target=search_for_pdfs, args=(query, int(num_results)))# Start the search in a separate thread to prevent blocking the UI
    search_thread.start()# Start the search in a separate thread to prevent blocking the UI

# Create the root window
root = tk.Tk()# Create the root window
root.title("PDF Downloader")# Set the title
root.geometry("500x400")  # Increased height to accommodate display
root.resizable(False, False)# Disable resizing

# Create a label
label = tk.Label(root, text="Enter your search query (topic):")# Create a label
label.pack()# Add the label to the window

# Create an entry widget
entry = tk.Entry(root, width=50)# Create an entry widget
entry.pack()# Add the entry widget to the window

# Create a label
label_2 = tk.Label(root, text="Enter the number of results you want:")# Create a label
label_2.pack()# Add the label to the window

# Create an entry widget
entry_2 = tk.Entry(root, width=50)# Create an entry widget
entry_2.pack()# Add the entry widget to the window

# Search button
search_button = tk.Button(root, text="Search", command=send_input, bg="green", fg="white", width=10, height=1, font=('Helvetica', '10', 'bold'))# Search button
search_button.pack()# Add the search button to the window

# Clear button
clear_button = tk.Button(root, text="Clear Display", command=clear_display, bg="blue", fg="white", width=15, height=1, font=('Helvetica', '10', 'bold'))# Clear button
clear_button.pack()# Add the clear button to the window

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=10, height=1, font=('Helvetica', '10', 'bold'))# Exit button
exit_button.pack()# Add the exit button to the window

# Text widget for displaying updates
display_text = tk.Text(root, height=10, width=50)# Text widget for displaying updates
display_text.pack()# Add the text widget to the window
display_text.config(state=tk.DISABLED)  # Disable editing
#icon
icon = tk.PhotoImage(file = "icon.png")#icon
root.iconphoto(False, icon)#icon

root.mainloop()# Start the main loop

#THE END OF THE CODE 😎 