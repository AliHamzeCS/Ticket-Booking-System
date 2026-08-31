from SettingsHistory import Load_Settings
from SettingsHistory import Dump_Settings
from Utils import decorator_func


# Change Currency
@decorator_func('Change Currency')
def change_currency():

    settings = Load_Settings()

    print(f"\nCurrent Currency : {settings['Currency']}")

    new_currency = input("Enter New Currency : ")

    settings['Currency'] = new_currency

    Dump_Settings(settings)

    print("\n✅ Currency changed successfully.")


# Change Screen Delay
@decorator_func('Change Screen Delay')
def change_screen_delay():

    settings = Load_Settings()

    print(f"\nCurrent Screen Delay : {settings['Screen Delay']} second(s)")

    try:
        new_delay = float(input("Enter New Screen Delay : "))

    except ValueError:
        print("❌ Enter only a number.")
        return

    if new_delay < 0:
        print("❌ Screen Delay cannot be negative.")
        return

    settings['Screen Delay'] = new_delay

    Dump_Settings(settings)

    print("\n✅ Screen delay changed successfully.")


# Show Current Settings
@decorator_func('Current Settings')
def show_settings():

    settings = Load_Settings()

    print('=' * 25)
    print('⚙️ CURRENT SETTINGS')
    print('=' * 25)

    print(f"\n💰 Currency     : {settings['Currency']}")
    print(f"⏱️ Screen Delay : {settings['Screen Delay']} second(s)\n")

    print('=' * 25)


# Reset Settings
@decorator_func('Reset Settings')
def reset_settings():

    settings = {
        'Currency': '$',
        'Screen Delay': 1
    }

    Dump_Settings(settings)

    print("✅ Settings have been reset to default.")