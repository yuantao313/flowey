// pages/canteen/canteen.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    canteen: {

    },
    restaurants: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: 'http://127.0.0.1:5000/getRestaurantByCid?id=' + options.id,
      success: (response) => {
        console.log(response.data)
        if (response.data["status"] != "success") {
          wx.showModal({
            cancelColor: 'cancelColor',
            title: "提示",
            content: "暂未开放，敬请期待！",
            success: (res) => {
              wx.navigateBack({
                delta: 1,
              })
            }
          })
        } else {
          wx.setNavigationBarTitle({
            title: response.data.canteen.name,
          })
          this.setData({
            restaurants: response.data.restaurants,
            canteen: response.data.canteen
          })
        }

      }
    })


  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})