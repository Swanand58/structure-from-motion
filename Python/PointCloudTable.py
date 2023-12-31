class PointCloudTable:
	def __init__(self):
		self.table = []
		self.entry_num = 0

	def init(self):
		self.table = []
		self.entry_num = 0

	def add_all_entries(self, two_d, three_d):
		size2d = len(two_d)
		three_d_start = len(three_d) - size2d
		print(size2d)
		print(len(three_d))
		print(three_d_start)

		for i in range(size2d):
			_two_d = (two_d[i].pt[0], two_d[i].pt[1])
			print(three_d[three_d_start+i])
			_three_d = (three_d[three_d_start + i][0],
						three_d[three_d_start + i][1],
						three_d[three_d_start + i][2])

			self.add_entry(_three_d, _two_d)

	def add_entry(self, three_d, two_d):
		e = (two_d, three_d)
		self.table.append(e)
		self.entry_num += 1

	def find_3d(self, two_d):
		for i in range(self.entry_num):
			if self.table[i][0][0] == two_d[0] and self.table[i][0][1] == two_d[1]:
				p = self.table[i][1]
				return p

		return None

	def copy(self):
		ret = PointCloudTable()
		ret.entry_num = self.entry_num
		for entry in self.table:
			ret.table.append(entry)

		return ret

	def table_size(self):
		return self.entry_num