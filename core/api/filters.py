import math

import django_filters
from django_filters import filters

from routerDetails.models import RouterDetail


class RouterFilter(django_filters.FilterSet):
    loopback = django_filters.CharFilter(method='filter_loopback')

    class Meta:
        model = RouterDetail

        fields = {
            'id', 'sap_id', 'internet_host_names', 'loopback', 'mac_address'
        }
    @staticmethod
    def convert_ipv4(ip):
        return tuple(int(n) for n in ip.split('.'))

    @staticmethod
    def check_ipv4_in(addr, start, end):
        return RouterFilter.convert_ipv4(start) < RouterFilter.convert_ipv4(addr) < RouterFilter.convert_ipv4(end)

    def filter_loopback(self, queryset, name, value):
        print("==>", value, name, "loop")
        print(queryset)
        is_range = "," in value
        if is_range:
            ip_list = value.split(",")
            num = ip_list[0].rsplit(".", 1)
            num2 = ip_list[1].rsplit(".", 1)

            for q in queryset:
                print(q.loopback)
                if not RouterFilter.check_ipv4_in(q.loopback, ip_list[0], ip_list[1]):
                    queryset = queryset.exclude(id=q.id)
        else:
            queryset = queryset.filter(loopback__contains=value)

            # ip_list = value.split(",")
            # num = ip_list[0].rsplit(".", 1)
            # num2 = ip_list[1].rsplit(".", 1)
            # print(ip_list, num, num2)
            # regex = ""
            # range1 = int(num[1])
            # range2 = int(num2[1])
            # numd0 = [int(x) for x in str(num[1])] if int(num[1]) > 10 else [int(num[1])]
            # numd1 = [int(x) for x in str(num2[1])] if int(num2[1]) > 10 else [int(num2[1])]
            # if range1 in range(0, 10) and range2 in range(0, 10):
            #     regex += "[{}-{}]".format(range1, range2)
            # if range1 in range(0, 10) and range2 not in range(0, 10):
            #     regex += "[{}-{}]".format(range1, "9")
            #
            # print(regex)
            # start = int(math.ceil(range1 / 10.0)) * 10
            # until = int(range2) - (int(range2) % 10)
            # print(start, until)
            #
            # init_regex = "[{}-{}]".format("0", "9")
            #
            # for i in range(start, until, 10):
            #
            #     if regex == "":
            #         if len(str(range1)) == len(str(range2)):
            #             regex += str(int(i / 10)) + "[{}-{}]".format(numd0[-1], numd1[-1])
            #         else:
            #             regex += str(int(i / 10)) + "[{}-{}]".format(numd0[-1], "9")
            #     else:
            #         regex += "|" + str(int(i / 10)) + init_regex
            #
            # # print("REGEX", regex)
            # add_or = ""
            # if range2 > 10:
            #     if regex != "":
            #         add_or = "|"
            #     regex += add_or + str(int(until / 10)) + "[{}-{}]".format("0", numd1[-1])
            # print("REGEX", regex)
            # regex = "(" + num[0] + "." + regex + ")"
            # print("REGEX", regex)
            #
            # queryset = queryset.filter(loopback__iregex=regex)
            # for q in queryset:
            #     print(q.id)
            #     r = q.loopback.rsplit(".", 1)
            #
            #     if int(r[1]) not in range(range1,range2+1):
            #         print(r)
            #         queryset = queryset.exclude(id=q.id)



        return queryset
