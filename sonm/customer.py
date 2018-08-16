import time
from typing import Optional

from .deal import Deal
from .order import Order
from .deal import Deal
from .task import Task, TaskParams
from .bid import BidParams


class Customer:
    def __init__(self):
        self.deal = Deal()
        self.order = Order()
        self.task = Task()

    def quick_start_task(self, ask_id: str, params: TaskParams, verbose=False) -> dict:
        """
        Create deal by means "quick_buy" and start task.
        :param ask_id:
        :param params:
        :param verbose: print debug info
        :return: task ID
        """
        deal = self.deal.quick_buy(ask_id)
        if verbose:
            print('Deal created. ID %s.' % deal['id'])  # TODO: logging

        task = self.task.start(
            deal_id=deal['id'],
            params=params,
        )
        if verbose:
            print('Task created. ID %s.' % task['id'])

        return task

    def start_task(self, bid: BidParams, task: TaskParams, verbose=False) -> dict:
        """
        Create bid-order, wait deal, create task
        :param bid:
        :param task:
        :param verbose:
        :return: create task ID
        """
        bid_id = Order().create(bid=bid)['id']
        if verbose:
            print('BID order created. ID %s.' % bid_id)

        # waiting deal for bid-order...
        while True:
            deal = self._get_deal_by_bid(bid_id)
            if deal:
                break   # got it!

            if verbose:
                print('Wait deal... Sleep 5 sec.')
            time.sleep(5)

        deal_id = deal['id']
        if verbose:
            print('Deal opened. ID %s.' % deal_id)

        task = Task().start(deal_id=deal_id, params=task)
        if verbose:
            print('Task created. ID %s.' % task['id'])

        return task

    def _get_deal_by_bid(self, bid_id: str) -> Optional[dict]:
        deals = Deal().list()['deals'] or []
        for deal in deals:
            if deal['bidID'] == bid_id:
                return deal
