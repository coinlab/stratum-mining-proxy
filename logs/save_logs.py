from subprocess import call


prefix = ''

try:
    open('w0.log').close()
    prefix = 'w'
except:
    pass

try:
    open('d0.log').close()
    prefix = 'd'
except:
    pass

try:
    open('s0.log').close()
    prefix = 's'
except:
    pass


print "Saving logs"
print "prefix = %s" % prefix

last_used_index = 0

for i in xrange(1, 100):
    try:
        open('%s0.log.%d' % (prefix, i)).close()
        last_used_index = i
    except Exception, e:
        pass  # print e

print prefix
print last_used_index


for i in xrange(0, 200):
    try:
        call(('mv %s%d.log %s%d.log.%d' % (prefix, i, prefix, i, last_used_index + 1)).split())
    except:
        pass

print "restarting forever"
call('forever restartall'.split())
