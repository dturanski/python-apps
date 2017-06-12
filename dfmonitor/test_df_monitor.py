"""
Copyright 2017 the original author or authors.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import unittest

import df_monitor


class TestDfMonitor(unittest.TestCase):
    def test_build_default_command(self):
        command = df_monitor.build_command(['df_monitor',
                                            '/var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log'])
        self.assertEqual(command,
                         'tail -f /var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log/stdout_0.log')

    def test_build_tail_n_command(self):

        command = df_monitor.build_command(['df_monitor',
                                            '/var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log',
                                            '-n 100'])
        self.assertEqual(command,
                         'tail -100 /var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log/stdout_0.log')

    def test_build_less_command(self):

        command = df_monitor.build_command(['df_monitor',
                                            '--less',
                                            '/var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log'])
        self.assertEqual(command,
                         'less /var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log/stdout_0.log')

    def test_build_command_with_instance(self):

        command = df_monitor.build_command(['df_monitor',
                                            '-i 3',
                                            '/var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log'])
        self.assertEqual(command,
                         'tail -f /var/folders/hd/5yqz2v2d3sxd3n879f4sg4gr0000gn/T/spring-cloud-dataflow-6604445305486891830/test-1496419405564/test.log/stdout_3.log')


    def test_search_log(self):
        info = df_monitor.search_url_info('test_data/sample.log')
        self.assertEqual({'username': 'user', 'url': 'http://localhost:58224', 'password': '53971881-d978-4230-8838-b82a68dfc851'}, info)


    def test_no_insufficient_args(self):
        try:
            df_monitor.build_command(['df_monitor'])
            self.fail('Should raise SystemExit')
        except:
            SystemExit



if __name__ == '__main__':
    unittest.main()
