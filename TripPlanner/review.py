import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from PIL import Image, ImageTk
import logging

class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)  # Call the constructor of the ttk.Frame class, passing the container widget (e.g., a parent frame)

        canvas = tk.Canvas(self)  # Create a canvas widget, which is used for scrolling
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)  # Create a vertical scrollbar associated with the canvas
        self.scrollable_frame = ttk.Frame(canvas)  # Create a frame inside the canvas to hold the scrollable content

        # Bind the <Configure> event to the function that adjusts the scroll region of the canvas

        self.scrollable_frame.bind(
            "<Configure>",  # When the size or position of the scrollable_frame changes
            lambda e:  # Define a lambda function with an event parameter 'e'
            canvas.configure(  # Configure the canvas widget
                scrollregion=canvas.bbox("all")  # Set the scroll region of the canvas
            )
        )

        # Create a window in the canvas to display the scrollable frame,
        # with an anchor at the northwest (top-left) corner
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configure the canvas to use the scrollbar for vertical scrolling
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas to the left side of the ScrollableFrame widget,
        # and make it fill both horizontally and vertically
        canvas.pack(side="left", fill="both", expand=True)

        # Pack the scrollbar to the right side of the ScrollableFrame widget,
        # and make it fill the vertical space
        scrollbar.pack(side="right", fill="y")

class TripPlannerApp:
    def __init__(self, root):
            # Initialize the TripPlannerApp class with the root window as the input
            self.root = root
            self.root.title("Trip Planner")  # Set the title of the root window to "Trip Planner"
            self.pending_image_path = None  # Variable to store the selected image path

            # Connect to MySQL database
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1927__sid",
                database="test"
            )
            self.db_cursor = self.db_connection.cursor()  # Create a cursor object to execute MySQL queries

            # Create custom style with background color
            self.style = ttk.Style()  # Initialize a ttk.Style object
            self.style.configure("Custom.TFrame", background="#111F4D")  # Configure a custom style for frames
            self.style.configure("Add.TButton", font=("Helvetica", 14))  # Configure a custom style for buttons

            # Create main frame
            self.main_frame = ttk.Frame(root, padding="20",
                                        style="Custom.TFrame")  # Create a main frame with custom style
            self.main_frame.grid(row=0, column=0, sticky="nsew")  # Grid layout manager for main frame

            # Create a label for the customer reviews
            ttk.Label(self.main_frame, text="Customer Reviews", font=("Arial", 24, "italic"),
                      background=("#111F4D"), foreground=("white")).grid(row=0, column=0, columnspan=3, pady=10)

            # Create a scrollable frame to hold the review entries
            self.scrollable_frame = ScrollableFrame(self.main_frame)
            self.scrollable_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

            # Add some sample reviews
            self.load_reviews()

            # Create entry for new review
            ttk.Label(self.main_frame, text="Your Review:", font=(10), background=("#111F4D"),
                      foreground=("white")).grid(row=2, column=0, sticky="e")
            self.new_review_entry = ttk.Entry(self.main_frame, width=40)  # Create an entry widget for user input
            self.new_review_entry.grid(row=2, column=1, padx=5, pady=5)  # Grid layout manager for entry widget

            # Create button for adding picture
            self.add_picture_button = ttk.Button(self.main_frame, text="Add Picture", command=self.add_picture,
                                                 style="Add.TButton")  # Create a button widget for adding pictures
            self.add_picture_button.grid(row=2, column=2, padx=5, pady=5)  # Grid layout manager for button

            # Create rating scale
            ttk.Label(self.main_frame, text="Rating:", font=(10), background=("#111F4D"),
                      foreground=("white")).grid(row=3, column=0, sticky="e")  # Label for rating scale
            self.rating_scale = tk.Scale(self.main_frame, from_=1, to=5, orient=tk.HORIZONTAL,
                                         length=150)  # Scale widget
            self.rating_scale.grid(row=3, column=1, columnspan=1, padx=5,
                                   pady=5)  # Grid layout manager for scale widget

            # Create button for adding review
            self.add_review_button = ttk.Button(self.main_frame, text="Add Review", command=self.add_new_review,
                                                style="Add.TButton")  # Button widget for adding reviews
            self.add_review_button.grid(row=6, column=1, columnspan=1, padx=5, pady=5)  # Grid layout manager for button

        # Other methods remain unchanged...

    def load_reviews(self):
        # Execute SQL query to select all reviews from the database
        self.db_cursor.execute("SELECT author, review, image_path, rating FROM reviews")
        # Fetch all the reviews from the database
        reviews = self.db_cursor.fetchall()
        # Iterate over each review fetched from the database
        for i, review in enumerate(reviews):
            # Unpack the values from the current review tuple
            author, review_text, image_path, rating = review
            # Display the current review by calling the display_review method
            self.display_review(author, review_text, rating, image_path, i)

    def add_picture(self):
        """Open a file dialog to select a picture."""
        # Open a file dialog to select a picture and get the selected file path
        file_path = filedialog.askopenfilename()
        # Store the selected image path temporarily
        self.pending_image_path = file_path

    def add_new_review(self):
        """Callback function for adding a new review."""
        # Get the text from the new review entry widget
        new_review_text = self.new_review_entry.get()
        # Get the rating from the rating scale widget
        rating = self.rating_scale.get()  # Get the rating
        # Check if the new review text is not empty
        if new_review_text:
            # If an image path is selected
            if self.pending_image_path:
                # Save the new review to the database by calling the save_review_to_database method
                self.save_review_to_database("You", new_review_text, rating, self.pending_image_path)
                # Clear the pending image path
                self.pending_image_path = None
            else:
                # Save the new review to the database without an image path
                self.save_review_to_database("You", new_review_text, rating)
            # Clear the new review entry widget after adding the review
            self.new_review_entry.delete(0, tk.END)  # Clear the entry widget

    def add_review(self, review, rating, author, image_path=None):
        """Add a new review to the scrollable frame."""
        # Get the number of existing reviews in the scrollable frame
        review_count = len(self.scrollable_frame.scrollable_frame.winfo_children())

        # Display the new review in the scrollable frame by calling the display_review method
        self.display_review(author, review, rating, image_path, review_count)

        # Update the scroll region of the canvas to reflect the changes
        self.update_scroll_region()

    def display_review(self, author, review_text, rating, image_path, row):
        """Display a review entry."""
        # Create a new frame to hold the review entry
        review_frame = ttk.Frame(self.scrollable_frame.scrollable_frame, padding=10, relief="groove")
        # Place the review frame in the scrollable frame at the specified row
        review_frame.grid(row=row, column=0, pady=10, sticky="ew")

        # Display the review text and author
        ttk.Label(review_frame, text=f"{author}: {review_text}", font=("Helvetica", 12, "bold")).grid(row=0, column=0,
                                                                                                      columnspan=2,
                                                                                                      sticky="w")
        # Display the rating
        ttk.Label(review_frame, text=f"Rating: {rating}", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w")

        # Display the picture if available
        if image_path:
            # Open the image file
            image = Image.open(image_path)
            # Resize the image to fit within a 100x100 pixel box
            image.thumbnail((100, 100))
            # Convert the image to a Tkinter-compatible format
            photo = ImageTk.PhotoImage(image)
            # Create a label to display the image
            picture_label = ttk.Label(review_frame, image=photo)
            picture_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
            # Place the picture label in the review frame
            picture_label.grid(row=1, column=1, padx=10, sticky="e")

    def update_scroll_region(self):
        """Update the scroll region of the canvas."""
        self.scrollable_frame.update_idletasks()  # Update the scrollable frame
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Update the scroll region of the canvas
    def save_review_to_database(self, author, review, rating, image_path=None):
        """Save a new review to the database."""
        try:
            # Execute an SQL query to insert the new review into the 'reviews' table
            query = "INSERT INTO reviews (author, review, rating, image_path) VALUES (%s, %s, %s, %s)"
            self.db_cursor.execute(query, (author, review, rating, image_path))
            # Commit the transaction to save the changes to the database
            self.db_connection.commit()
            logging.info("Review added successfully.")
        except mysql.connector.Error as error:
            # If an error occurs during database operation, log the error
            logging.error("Failed to add review: %s", error)
            # Optionally, raise the exception to propagate it further
            raise

    def save_picture_to_database(self, file_path):
        try:
            # Get the ID of the latest review
            self.db_cursor.execute("SELECT MAX(id) FROM reviews")
            latest_review_id = self.db_cursor.fetchone()[0]

            if latest_review_id is not None:
                # Update the image_path field of the latest review
                self.db_cursor.execute("""
                    UPDATE reviews 
                    SET image_path = %s 
                    WHERE id = %s
                """, (file_path, latest_review_id))
                # Commit the transaction to save the changes to the database
                self.db_connection.commit()
            else:
                # Handle the case where there are no reviews in the database
                logging.warning("No reviews found in the database.")
        except mysql.connector.Error as error:
            # If an error occurs during database operation, log the error
            logging.error("Failed to save picture: %s", error)
            # Optionally, raise the exception to propagate it further
            raise


def main():
    # Create the root window of the application
    root = tk.Tk()
    # Create an instance of the TripPlannerApp class, passing the root window as an argument
    app = TripPlannerApp(root)
    # Start the Tkinter event loop to run the application
    root.mainloop()



if __name__ == "__main__":
    # Check if the script is being run as the main module
    # If so, execute the following block of code

    # Call the main function to start the application
    main()
