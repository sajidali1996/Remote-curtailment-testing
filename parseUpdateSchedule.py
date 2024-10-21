import struct
from datetime import datetime
path='C:\Users\Sajid Ali\Documents\RC testing\binary Files\github-repo\update-schedule.bin'
def decode_update_schedule(path):
    with open(path, 'rb') as f:
        # Read Schedule ID (10 bytes)
        schedule_id = f.read(10).decode('utf-8').strip()
        
        # Read Power Plant ID (26 bytes)
        power_plant_id = f.read(26).decode('utf-8').strip()
        
        # Read Control DateTime (12 bytes: YYYYMMDDHHMM)
        raw_time = f.read(12).decode('utf-8').strip()
        try:
            control_datetime = datetime.strptime(raw_time, '%Y%m%d%H%M')
        except ValueError as e:
            print(f"Invalid Control DateTime format: {raw_time}")
            raise e
        
        # Read number of output control rate data (4 bytes)
        num_output_control_rate_data = struct.unpack('I', f.read(4))[0]
        
        # Read Output Control Rate (num_output_control_rate_data bytes)
        output_control_rate = list(struct.unpack(f'{num_output_control_rate_data}B', f.read(num_output_control_rate_data)))
        
        # Read Fixed Schedule Update Flag (1 byte)
        fixed_schedule_update_flag = struct.unpack('B', f.read(1))[0]
        
        # Read Checksum (2 bytes)
        checksum = struct.unpack('H', f.read(2))[0]
        
        # Read Next Access DateTime (14 bytes: YYYYMMDDHHMMSS)
        raw_next_time = f.read(14).decode('utf-8').strip()
        try:
            next_access_datetime = datetime.strptime(raw_next_time, '%Y%m%d%H%M%S')
        except ValueError as e:
            print(f"Invalid Next Access DateTime format: {raw_next_time}")
            raise e
        
        # Display the decoded data
        data = {
            "ScheduleID": schedule_id,
            "PowerPlantID": power_plant_id,
            "ControlDateTime": control_datetime,
            "NumOutputControlRateData": num_output_control_rate_data,
            "OutputControlRate": output_control_rate,
            "FixedScheduleUpdateFlag": fixed_schedule_update_flag,
            "Checksum": checksum,
            "NextAccessDateTime": next_access_datetime
        }
        
        return data

# Example usage
file_path = 'path_to_your_file.bin'  # Replace with your binary file path
update_schedule_data = decode_update_schedule(file_path)
print(update_schedule_data)
