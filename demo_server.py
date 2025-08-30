import genie_tts as genie

# Start server
genie.start_server(
    host="0.0.0.0",  # Host address
    port=9999,  # Port
    workers=1  # Number of workers
)