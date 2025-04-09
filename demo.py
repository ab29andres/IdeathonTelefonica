from opengateway_sandbox_sdk import SimSwap, NumberVerification, DeviceLocation, ClientCredentials

credentials = ClientCredentials(
    client_id="a9d4e524-851c-41f2-a18f-8eb9be698bb0",
    client_secret="e3d05194-b31a-43de-9f72-527123b6cbda"
)

operator_code = "telefonica-sandbox"

sim_swap = SimSwap(credentials, code=operator_code)
number_verification = NumberVerification(credentials, code=operator_code)
device_location = DeviceLocation(credentials, code=operator_code)

phone_number = "+34600000001"

print("Verificando número de teléfono...")
try:
    result = number_verification.verify(phone_number=phone_number)
    print("Resultado Number Verification:", result)
except Exception as e:
    print("Error en verificación del número:", e)

