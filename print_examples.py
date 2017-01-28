from nemreader import MeterRecord


def print_meter_record(file_path):
    m = MeterRecord(file_path)
    print(m.NMI, m.NMI_configuration)
    for channel in m.readings.keys():
        print('Channel', channel)
        for reading in m.readings[channel][-5:]:
            print(reading)


if __name__ == '__main__':
    print('NEM13 Example:')
    print_meter_record('examples/NEM13#DATA_14121801#WBAYM#3044076134.V01')

    print('NEM12 Example:')
    print_meter_record('examples/NEM12#DATA_16081001#WBAYM#3044076134.V01')