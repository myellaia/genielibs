import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.nat.configure import unconfigure_static_nat_outside_rule


class TestUnconfigureStaticNatOutsideRule(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Stargazer:
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
        self.device = self.testbed.devices['Stargazer']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_static_nat_outside_rule(self):
        result = unconfigure_static_nat_outside_rule(self.device, '10.1.1.1', '192.168.1.1')
        expected_output = None
        self.assertEqual(result, expected_output)
