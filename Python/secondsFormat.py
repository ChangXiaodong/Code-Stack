def timeFormat(seconds):
        '''
        Parameter：

        Function：
                               格式化时间
        :type seconds:输入时间的秒数
		:rtype:返回特定时间格式
        Autor:xiaoxiami 2015.11.29
        Others：
        '''
        if seconds < 60:
            return str(seconds) + " 秒"
        elif seconds < 3600:
            return str(seconds / 60) + " 分 " + str(seconds % 60) + " 秒"
        elif seconds < 86400:
            hour = seconds / 3600
            seconds %= 3600
            minutes = seconds / 60
            return str(hour) + " 小时 " + str(minutes) + " 分 " + str(seconds % 60) + " 秒"
        else:
            days = seconds / 86400
            seconds %= 86400
            hours = seconds / 3600
            seconds %= 3600
            minutes = seconds / 60
            return str(days) + " 天 " + str(hours) + " 小时 " + str(minutes) + " 分 " + str(seconds % 60) + " 秒"