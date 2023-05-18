#!/bin/bash

# Run daily-ioc.py
python3 daily-ioc.py

# Check if the previous command succeeded
if [ $? -eq 0 ]; then
  echo "daily-ioc.py completed successfully."

  # Run gitpush.sh
  ./gitpush.sh
else
  echo "daily-ioc.py failed to execute. Aborting gitpush.sh."
fi
