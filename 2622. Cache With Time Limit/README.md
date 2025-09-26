[Problem](https://leetcode.com/problems/cache-with-time-limit/)

This problem only allows to submit in either JavaScript or TypeScript.

## Timestamp (Lazy Expiration) Solution

This approach is based on the **lazy deletion** strategy. We remove the expired entries only when the methods (`get(...)`, `set(...)`, `count()`) are called. It's straightforward and scales better (no thousands of timers running in the background). However, the `count()` method requires to iterate over the entire cache, which takes $O(n)$ time.


- [Submission](https://leetcode.com/problems/cache-with-time-limit/submissions/1783679671/) (Runtime: 32 ms, Memory: 54.6 MB)
- TC: $O(1)$ (for `get(...)` and `set(...)`), $O(n)$ (for `count()`)
- SC: $O(n)$, for cache

Below is the TypeScript code.

```ts
class TimeLimitedCache {
    private cache: Map<number, [value: number, expAt: number]>;

    constructor() {
        this.cache = new Map();
    }

    set(key: number, value: number, duration: number): boolean {
        const now = Date.now();
        const existedAndValid = this.cache.has(key) && this.cache.get(key)[1] > now;
        this.cache.set(key, [value, now + duration]);

        return existedAndValid;
    }

    get(key: number): number {
        const now = Date.now();

        const entry = this.cache.get(key);
        if (!entry) return -1;

        const [val, exp_time] = entry;
        if (exp_time <= now) {
            this.cache.delete(key);
            return -1;
        }

        return val;
    }

    count(): number {
        const now = Date.now();
        const toDelete: number[] = []

        // collect then delete to avoid mutating while iterating
        for (const [k, [v, exp_t]] of this.cache) {
            if (exp_t <= now) toDelete.push(k);
        }
        for (const k of toDelete) this.cache.delete(k);
        return this.cache.size
    }
}


/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

```


## Timer (Active Expiration) Solution


This approach relies on the **event-driven** strategy. We use timers to remove the expired entries automatically, which aligns well with the JavaScript event loop.

The idea is that when we **set**, we need to schedule a timer to remove the entry after the duration. When we are **resetting** the value (key already exists), we need to clear the existing timer and schedule a new one.

In this method, the `count()` method only takes $O(1)$ time since keys are removed automatically and we don't need to iterate over the entire cache. However, when there are thousands of keys, memory/CPU overhead and event-loop churns could be a concern due to lots of timers running in the background.


- [Submission](https://leetcode.com/problems/cache-with-time-limit/submissions/1783687484/) (Runtime: 55 ms, Memory: 55.7 MB)
- TC: $O(1)$ for all methods
- SC: $O(n)$, for cache



```ts
class TimeLimitedCache {
    private data = new Map<number, number>();             // key -> value
    private timers = new Map<number, ReturnType<typeof setTimeout>>(); // key -> timeout
    private expiries = new Map<number, number>();         // key -> expiresAt (for return semantics)
    private activeCount = 0;

    set(key: number, value: number, duration: number): boolean {
        const now = Date.now();
        const expiresAt = now + duration;
        const existedAndValid = this.expiries.has(key) && (this.expiries.get(key)! > now);

        // Clear existing timer if any
        const oldTimer = this.timers.get(key);
        if (oldTimer) clearTimeout(oldTimer);

        // (Re)store value & expiry
        this.data.set(key, value);
        this.expiries.set(key, expiresAt);

        // If it was expired or new, we are (re)activating it => ensure it's counted
        if (!existedAndValid) this.activeCount++;

        // Schedule removal
        const t = setTimeout(() => {
            // Remove only if this expiry is still current (ignore stale timers)
            if (this.expiries.get(key) === expiresAt) {
                this.data.delete(key);
                this.expiries.delete(key);
                this.timers.delete(key);
                this.activeCount--;
            }
        }, duration);

        this.timers.set(key, t);
        return existedAndValid;
    }

    get(key: number): number {
        const now = Date.now();
        const exp = this.expiries.get(key);
        if (exp === undefined || exp <= now) return -1;  // if timer hasn't fired yet but logically expired
        return this.data.get(key)!;
    }

    count(): number {
        return this.activeCount;
    }
}

```