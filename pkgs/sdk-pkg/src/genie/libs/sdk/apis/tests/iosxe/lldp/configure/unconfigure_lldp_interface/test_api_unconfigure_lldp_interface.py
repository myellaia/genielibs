import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.lldp.configure import unconfigure_lldp_interface


class TestUnconfigureLldpInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Cat9600HA_DUT1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9600
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Cat9600HA_DUT1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_lldp_interface(self):
        result = unconfigure_lldp_interface(self.device, 'Twe2/0/15')
        expected_output = None
        self.assertEqual(result, expected_output)
