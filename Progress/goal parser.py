class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """

        my_dict = {"G":"G","()":'o',"(al)":"al"}

        for key in my_dict:
            if key in command:
                command = command.replace(key,my_dict[key])
            
        return command