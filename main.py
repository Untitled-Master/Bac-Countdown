from datetime import datetime
from PIL import Image, ImageDraw


# Calculate the number of days between two dates
def calculate_days_left(target_date):
  today = datetime.now()
  days_left = (target_date - today).days
  return max(days_left, 0)


# Create a progress bar image without text
def create_progress_bar(percentage):
  # Define the width and height of the progress bar image
  width = 300
  height = 30

  # Create a white background image
  image = Image.new("RGB", (width, height), "white")
  draw = ImageDraw.Draw(image)

  # Calculate the width of the progress bar based on the percentage
  bar_width = int(width * (percentage / 100))

  # Draw the progress bar
  draw.rectangle([0, 0, bar_width, height], fill="green")

  return image


# Define the target date and time
target_date = datetime(2024, 6, 12, 8, 0, 0)

# Calculate the days left until the target date
days_left = calculate_days_left(target_date)

# Calculate the percentage of days left
total_days = (target_date - datetime(2023, 9, 21, 0, 0, 0)).days
percentage = ((total_days - days_left) / total_days) * 100

# Create the progress bar image without text
progress_bar_image = create_progress_bar(percentage)

# Save the image
image_filename = "progress_bar.png"
progress_bar_image.save(image_filename)
progress_bar_image.show()
# Display the progress bar image
# You can use your own method for this, as it seems you are using a custom sendLocalImage method
# Replace the following line with your actual code to send the image
print(f"Days left until BAC 2024: {days_left} days")
print(f"Percentage progress: {percentage:.2f}%")
