def validate_data(log_df, dbc):
    errors = []

    for _, row in log_df.iterrows():
        try:
            message = dbc.get_message_by_frame_id(row['ID'])
            decoded_data = message.decode(bytes.fromhex(row['Data'].replace(' ', '')))

            for signal_name, value in decoded_data.items():
                signal = message.get_signal(signal_name)
                if value < signal.minimum or value > signal.maximum:
                    errors.append({
                        "Timestamp": row['Time'],
                        "ID": row['ID'],
                        "Signal": signal_name,
                        "Value": value,
                        "Error": f"Value out of range ({signal.minimum} - {signal.maximum})",
                    })
        except Exception as e:
            errors.append({
                "Timestamp": row['Time'],
                "ID": row['ID'],
                "Error": str(e)
            })

    return errors