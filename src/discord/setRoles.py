import discord
import numpy as np
import dataManagement

class RolePreferenceSelect(discord.ui.View):
    # Select menu for choosing your role preferences
    role_pref = np.empty(5, dtype=int)
    role_pref.fill(5)
    role_counter = 0

    @discord.ui.select(
        placeholder="Carry Preference", max_values=1,
        options=[
            discord.SelectOption(label="Very high", value="5"),
            discord.SelectOption(label="High", value="4"),
            discord.SelectOption(label="Moderate", value="3"),
            discord.SelectOption(label="Low", value="2"),
            discord.SelectOption(label="Very low", value="1"),
        ]
    )
    async def select_carry_preference(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.role_pref[0] = str(select_item.values[0])
        self.role_counter += 1
        if self.role_counter == 5:
            current_user = str(interaction.user.id)
            dataManagement.update_roles(current_user, self.role_pref)
            await interaction.response.defer()
            await interaction.followup.edit_message(interaction.message.id,
                                                    content="Thank you for updating your preferences",
                                                    view=None)
        else:
            await interaction.response.defer()

    @discord.ui.select(
        placeholder="Midlane Preference", max_values=1,
        options=[
            discord.SelectOption(label="Very high", value="5"),
            discord.SelectOption(label="High", value="4"),
            discord.SelectOption(label="Moderate", value="3"),
            discord.SelectOption(label="Low", value="2"),
            discord.SelectOption(label="Very low", value="1"),
        ]
    )
    async def select_mid_preference(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.role_pref[1] = str(select_item.values[0])
        self.role_counter += 1
        if self.role_counter == 5:
            current_user = str(interaction.user.id)
            dataManagement.update_roles(current_user, self.role_pref)
            await interaction.response.defer()
            await interaction.followup.edit_message(interaction.message.id,
                                                    content="Thank you for updating your preferences",
                                                    view=None)
        else:
            await interaction.response.defer()

    @discord.ui.select(
        placeholder="Offlane Preference", max_values=1,
        options=[
            discord.SelectOption(label="Very high", value="5"),
            discord.SelectOption(label="High", value="4"),
            discord.SelectOption(label="Moderate", value="3"),
            discord.SelectOption(label="Low", value="2"),
            discord.SelectOption(label="Very low", value="1"),
        ]
    )
    async def select_off_preference(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.role_pref[2] = str(select_item.values[0])
        self.role_counter += 1
        if self.role_counter == 5:
            current_user = str(interaction.user.id)
            dataManagement.update_roles(current_user, self.role_pref)
            await interaction.response.defer()
            await interaction.followup.edit_message(interaction.message.id,
                                                    content="Thank you for updating your preferences",
                                                    view=None)
        else:
            await interaction.response.defer()

    @discord.ui.select(
        placeholder="Soft Support Preference", max_values=1,
        options=[
            discord.SelectOption(label="Very high", value="5"),
            discord.SelectOption(label="High", value="4"),
            discord.SelectOption(label="Moderate", value="3"),
            discord.SelectOption(label="Low", value="2"),
            discord.SelectOption(label="Very low", value="1"),
        ]
    )
    async def select_soft_preference(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.role_pref[3] = str(select_item.values[0])
        self.role_counter += 1
        if self.role_counter == 5:
            current_user = str(interaction.user.id)
            dataManagement.update_roles(current_user, self.role_pref)
            await interaction.response.defer()
            await interaction.followup.edit_message(interaction.message.id,
                                                    content="Thank you for updating your preferences",
                                                    view=None)
        else:
            await interaction.response.defer()

    @discord.ui.select(
        placeholder="Hard Support Preference", max_values=1,
        options=[
            discord.SelectOption(label="Very high", value="5"),
            discord.SelectOption(label="High", value="4"),
            discord.SelectOption(label="Moderate", value="3"),
            discord.SelectOption(label="Low", value="2"),
            discord.SelectOption(label="Very low", value="1"),
        ]
    )
    async def select_hard_preference(self, interaction: discord.Interaction, select_item: discord.ui.Select):
        self.role_counter += 1
        self.role_pref[4] = str(select_item.values[0])
        if self.role_counter == 5:
            current_user = str(interaction.user.id)
            dataManagement.update_roles(current_user, self.role_pref)
            await interaction.response.defer()
            await interaction.followup.edit_message(interaction.message.id,
                                                    content="Thank you for updating your preferences",
                                                    view=None)
        else:
            await interaction.response.defer()