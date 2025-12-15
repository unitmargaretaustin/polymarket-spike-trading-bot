import time

class SpikeScanner:
    def __init__(self, settings, logger):
        self.settings = settings
        self.logger = logger
        self.last_trade_ts = {}

    def scan_markets(self):
        for market in self.settings["markets"]:
            if self._in_cooldown(market["id"]):
                continue

            snapshot = self._fetch_market_snapshot(market)
            spike = self._detect_spike(snapshot, market)

            if spike and self._liquidity_ok(snapshot, market):
                self._execute_trade(market, spike)

    def _fetch_market_snapshot(self, market):
        # Placeholder for browser/API read
        return {
            "price": 0.54,
            "prev_price": 0.49,
            "spread": 0.01,
            "liquidity": 1200
        }

    def _detect_spike(self, snapshot, market):
        delta = snapshot["price"] - snapshot["prev_price"]
        pct = delta / snapshot["prev_price"]

        threshold = market["spike_threshold_pct"]
        if abs(pct) >= threshold:
            direction = "BUY" if pct > 0 else "SELL"
            return {"direction": direction, "pct": pct}

        return None

    def _liquidity_ok(self, snapshot, market):
        if snapshot["liquidity"] < market["min_liquidity"]:
            return False
        if snapshot["spread"] > market["max_spread"]:
            return False
        return True

    def _execute_trade(self, market, spike):
        self.logger.info(
            f"Spike detected on {market['name']} | "
            f"Direction: {spike['direction']} | Move: {spike['pct']:.2%}"
        )

        # Placeholder for order placement
        self.last_trade_ts[market["id"]] = time.time()

    def _in_cooldown(self, market_id):
        cooldown = self.settings["trade_cooldown_seconds"]
        last_ts = self.last_trade_ts.get(market_id)

        if not last_ts:
            return False

        return (time.time() - last_ts) < cooldown
