import tkinter as tk
import json
import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'


def submitFunction():
    # pulls the information from the input fields 
    api_key = apiEntry.get()
    
    hashsum = hashEntry.get()
    # clears our output field incase there is text entered there
    responseText.delete(1.0, tk.END)

    #MD5SUMs are always 32 characters in length
    if len(hashsum) != 32:
        responseText.insert(tk.END, "Hash must be 32 characters in length.")

    else:
        params = {'apikey': api_key, 'resource': hashsum}

        response = (requests.get(url, params=params))

        # Run a try catch statement. If the command fails to work, it is because the api responds with an error that isn't json parsable, typically due to an invalid API key
        try:
            response = response = json.loads(response.text)
            # After converting the above into a python dictionary format, we can check the positives key for the total number of sites that are malicious
            try:
                if (response['positives'] > 5):
                    responseText.insert(tk.END, "The file of that hash is malicious.")
                elif (response['positives'] > 0):
                    responseText.insert(tk.END, "The file of that hash is potentially malicious")
                else:
                    responseText.insert(tk.END, "The file of that hash is not malicious")
            except:
                responseText.insert(tk.END, "Hash not found.")

        except:
            responseText.insert(tk.END, "Invalid API Key.")

    #responseText.insert(tk.END, api_key)

    


### Build out the GUI
##Creates the window
window = tk.Tk()
window.title("Virus Total Checker")
window.geometry('500x250')
window.resizable(False, False)

## Creates a header above the input fields
titleLabel = tk.Label(text = "Virus Total Checker")
titleLabel.pack()

## Creates the entry fields for api_key
apiLabel = tk.Label(text = "Enter your API Key:")
apiLabel.pack()
apiEntry = tk.Entry(fg="black", bg="white", width=100)
apiEntry.pack()

## Creates entry fields for the md5sum hash
hashLabel = tk.Label(text = "Enter the MD5sum:")
hashLabel.pack()
hashEntry = tk.Entry(fg="black", bg="white", width=32)
hashEntry.pack()

## Sets up a frame to contain both buttons, and place them side by side
button_frame = tk.Frame(master=window)
btn_submit = tk.Button(text="Submit", master=button_frame, command=submitFunction) # Calls the function to check the hash and api key when clicked
btn_cancel = tk.Button(text="Cancel", master=button_frame, command=window.destroy) # command = window.destroy exits the window
btn_submit.pack(side='left')
btn_cancel.pack(side='right')
button_frame.pack()

## Sets up the field where the server response will be put
responseText = tk.Text(window)
responseText.pack()


tk.mainloop()

