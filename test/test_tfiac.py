from tfiac import Tfiac, ON_MODE, OPERATION_MODE, TARGET_TEMP
from time import sleep
import unittest

HOST = '192.168.1.108'


OPERATION_LIST = ['heat', 'selfFeel', 'dehumi', 'fan', 'cool']
FAN_LIST = ['Auto', 'Low', 'Middle', 'High']
SWING_LIST = [
    'Off',
    'Vertical',
    'Horizontal',
    'Both',
]

MIN_TEMP = 73
MAX_TEMP = 88

SHORT_WAIT = 2
LONG_WAIT = 3

class TfiacTest(unittest.TestCase):
    def setUp(self):
        self.tfiac = Tfiac(HOST)

    def test_init(self):
        sleep(SHORT_WAIT)
        status = self.tfiac.status
        self.assertTrue(status.get(ON_MODE))
        print ("Current status is {}".format(status[ON_MODE]))
        self.assertIn(status[ON_MODE], ['on', 'off'])

    def switch(self, tfiac, on_off):
        tfiac.set_state(ON_MODE, on_off)
        sleep(SHORT_WAIT)
        tfiac.update()
        self.assertEqual(tfiac.status[ON_MODE], on_off)
    
    def test_power(self):
        self.switch(self.tfiac, 'off')
        sleep(SHORT_WAIT)
        self.switch(self.tfiac, 'on')
        sleep(SHORT_WAIT)
        self.switch(self.tfiac, 'off')
        sleep(SHORT_WAIT)
    
    def change_operative_mode(self, tfiac, mode):
        tfiac.set_state(OPERATION_MODE, mode)
        sleep(SHORT_WAIT)
        tfiac.update()
        self.assertEqual(tfiac.status[OPERATION_MODE], mode)

    def test_operation_modes(self):
        self.switch(self.tfiac, 'on')
        for mode in OPERATION_LIST:
            self.change_operative_mode(self.tfiac, mode)
            sleep(LONG_WAIT)
        self.switch(self.tfiac, 'off')
        sleep(LONG_WAIT)

    
    def set_temp(self, tfiac, temperature):
        tfiac.set_state(TARGET_TEMP, temperature)
        sleep(LONG_WAIT)
        tfiac.update()
        self.assertAlmostEqual(tfiac.status[TARGET_TEMP], temperature, 0, "Tried to set {} and got {}".format(temperature,
            tfiac.status[TARGET_TEMP]))

    def test_temperatures(self):
        self.switch(self.tfiac, 'on')
        for curr_mode in ['heat', 'selfFeel', 'cool']:
            self.change_operative_mode(self.tfiac, curr_mode)
            self.set_temp(self.tfiac, MIN_TEMP)
            sleep(LONG_WAIT)
            self.set_temp(self.tfiac, MAX_TEMP)
            sleep(LONG_WAIT)
            middle_point = int((MIN_TEMP+MAX_TEMP)/2)
            self.set_temp(self.tfiac, middle_point)
            sleep(LONG_WAIT)
            for incr_temp in range(middle_point-3, middle_point+2):
                self.set_temp(self.tfiac, incr_temp)
                sleep(SHORT_WAIT)
        self.switch(self.tfiac, 'off')


if __name__ == '__main__':
    unittest.main()