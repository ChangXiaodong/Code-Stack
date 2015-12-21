def timeFormat(seconds):
        '''
        Parameter��

        Function��
                               ��ʽ��ʱ��
        :type seconds:����ʱ�������
		:rtype:�����ض�ʱ���ʽ
        Autor:xiaoxiami 2015.11.29
        Others��
        '''
        if seconds < 60:
            return str(seconds) + " ��"
        elif seconds < 3600:
            return str(seconds / 60) + " �� " + str(seconds % 60) + " ��"
        elif seconds < 86400:
            hour = seconds / 3600
            seconds %= 3600
            minutes = seconds / 60
            return str(hour) + " Сʱ " + str(minutes) + " �� " + str(seconds % 60) + " ��"
        else:
            days = seconds / 86400
            seconds %= 86400
            hours = seconds / 3600
            seconds %= 3600
            minutes = seconds / 60
            return str(days) + " �� " + str(hours) + " Сʱ " + str(minutes) + " �� " + str(seconds % 60) + " ��"