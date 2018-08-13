from .deal import Deal
from .order import Order
from .task import Task, TaskParams


class Customer:
    def __init__(self):
        self.deal = Deal()
        self.order = Order()
        self.task = Task()

    def quick_start_task(self, ask_id: str, params: TaskParams, verbose=False) -> str:
        """
        Create deal by means "quick_buy" and start task.
        :param ask_id:
        :param params:
        :param verbose: print debug info
        :return: task ID
        """
        deal = self.deal.quick_buy(ask_id)
        if verbose:
            print('Deal created. ID %s.' % deal['id'])

        task = self.task.start(
            deal_id=deal['id'],
            params=params,
        )
        if verbose:
            print('Task created. ID %s.' % task['id'])

        return task['id']
