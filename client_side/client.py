import pandas as pd
import websocket


def on_message(ws, message):
    print("Receiving DF")
    dataframe_person = pd.read_json(message)
    print(dataframe_person.head())
    dataframe_person.to_csv(
        "data.csv",
        mode='a',
        header=False,
        index=False
    )


ws = websocket.WebSocketApp(
    "ws://localhost:8000",
    on_message=on_message
)
ws.run_forever()
