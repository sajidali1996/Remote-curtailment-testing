function data = decode_update_schedule()
   fid = fopen('update-schedule.bin', 'rb');
    % Check if the file identifier is valid
    if fid == -1
        error('File could not be opened');
    end

    % Parse Update Schedule [Format No 203]
    data.ScheduleID = fread(fid, 10, '*char')';    % 10 Byte Schedule ID
    data.PowerPlantID = fread(fid, 40, '*char')';  % 26 Byte Power Plant ID
    
    % Date and time of control (12 bytes: YYYYMMDDhhmm)
    raw_time = fread(fid, 12, '*char')'; 
    raw_time = strtrim(raw_time);  % Trim any whitespace
    
    % Debug: Check raw_time contents
    fprintf('Raw Control DateTime: %s\n', raw_time);
    
    % Check if raw_time is valid before converting
    if all(raw_time >= '0' & raw_time <= '9')
        data.ControlDateTime = datetime(raw_time, 'InputFormat', 'yyyyMMddHHmm');
    else
        error('Invalid Control DateTime format: %s', raw_time);
    end
    
    % Number of output control rate data (5 Bytes)
    data.NumOutputControlRateData = fread(fid, 1, 'uint32');
    
    % Output control rate (1 byte per data, repeated)
    data.OutputControlRate = fread(fid, data.NumOutputControlRateData, 'uint8');
    
    % Fixed Schedule Update Flag (1 Byte)
    data.FixedScheduleUpdateFlag = fread(fid, 1, 'uint8');
    
    % Checksum (2 Bytes)
    data.Checksum = fread(fid, 2, 'uint8');
    
    % Next access date and time (14 bytes: YYYYMMDDhhmmss)
    raw_next_time = fread(fid, 14, '*char')'; 
    raw_next_time = strtrim(raw_next_time);  % Trim any whitespace
    
    % Debug: Check raw_next_time contents
    fprintf('Raw Next Access DateTime: %s\n', raw_next_time);
    
    % Check if raw_next_time is valid before converting
    if all(raw_next_time >= '0' & raw_next_time <= '9')
        data.NextAccessDateTime = datetime(raw_next_time, 'InputFormat', 'yyyyMMddHHmmss');
    else
        error('Invalid Next Access DateTime format: %s', raw_next_time);
    end
end
