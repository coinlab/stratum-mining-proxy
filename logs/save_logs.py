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


print "prefix = %s" % prefix

unused_index = 0

for i in xrange(1, 100):
    try:
        open('%s0.log.%d' % (prefix, i)).close()
    except Exception, e:
        print e
        unused_index = i
        break

print prefix
print unused_index


for i in xrange(0, 200):
    try:
        call(('mv %s%d.log %s%d.log.%d' % (prefix, i, prefix, i, unused_index)).split())
    except:
        pass


