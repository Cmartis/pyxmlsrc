#!/usr/bin/python3
import redis
r = redis.Redis()
r.mset({"croatia":"zagreb", "bahamas":"nassau"})
print(r.get("bahamas"))


