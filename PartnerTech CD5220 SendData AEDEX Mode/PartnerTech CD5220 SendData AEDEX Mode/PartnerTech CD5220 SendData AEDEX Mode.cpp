#include <windows.h>
#include <iostream>
#include <string>

void sendDataWithRTSCTS(const char* portName, const std::string& data) {
    HANDLE hSerial = CreateFileA(
        portName,
        GENERIC_READ | GENERIC_WRITE,
        0,
        NULL,
        OPEN_EXISTING,
        0,
        NULL
    );

    if (hSerial == INVALID_HANDLE_VALUE) {
        std::cerr << "Error opening serial port!" << std::endl;
        return;
    }

    DCB dcbSerialParams = { 0 };
    dcbSerialParams.DCBlength = sizeof(dcbSerialParams);

    if (!GetCommState(hSerial, &dcbSerialParams)) {
        std::cerr << "Error getting serial port state!" << std::endl;
        CloseHandle(hSerial);
        return;
    }

    dcbSerialParams.BaudRate = CBR_9600;
    dcbSerialParams.ByteSize = 8;
    dcbSerialParams.StopBits = ONESTOPBIT;
    dcbSerialParams.Parity = NOPARITY;

    dcbSerialParams.fRtsControl = RTS_CONTROL_HANDSHAKE;
    dcbSerialParams.fOutxCtsFlow = TRUE;

    if (!SetCommState(hSerial, &dcbSerialParams)) {
        std::cerr << "Error setting serial port state!" << std::endl;
        CloseHandle(hSerial);
        return;
    }

    COMMTIMEOUTS timeouts = { 0 };
    timeouts.ReadIntervalTimeout = 50;
    timeouts.ReadTotalTimeoutConstant = 50;
    timeouts.WriteTotalTimeoutConstant = 50;
    if (!SetCommTimeouts(hSerial, &timeouts)) {
        std::cerr << "Error setting timeouts!" << std::endl;
        CloseHandle(hSerial);
        return;
    }

    DWORD bytesWritten;
    if (!WriteFile(hSerial, data.c_str(), data.length(), &bytesWritten, NULL)) {
        std::cerr << "Error writing to serial port!" << std::endl;
    }
    else {
        std::cout << "Data sent: " << data << std::endl;
    }

    char buffer[256] = { 0 };
    DWORD bytesRead;
    if (ReadFile(hSerial, buffer, sizeof(buffer) - 1, &bytesRead, NULL)) {
        buffer[bytesRead] = '\0';
    }
    else {
        std::cerr << "Error reading from serial port!" << std::endl;
    }

    CloseHandle(hSerial);
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <COM_port> <message>" << std::endl;
        std::cout << "Manual can be found at https://github.com/Bw11111/PartnerTech-CD5220." << std::endl;
        return 1;
    }

    const char* portName = argv[1];
    std::string data;
    for (int i = 2; i < argc; ++i) {
        data += argv[i];
        if (i < argc - 1) {
            data += " ";
        }
    }

    std::string command = data + "\r";
    sendDataWithRTSCTS(portName, command);

    std::cout << "Program terminated." << std::endl;
    return 0;
}
